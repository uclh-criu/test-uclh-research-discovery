(function() {
    function displaySearchResults(results, store) {
      var searchResults = document.getElementById('search-results');

      Handlebars.registerHelper('truncate', function(content, length){
        return content.substring(0,length - 3) + '...'
      })
  
      if (results.length) { // Are there any results?
        var appendString = '';
  
        for (var i = 0; i < results.length; i++) {  // Iterate over the results
          var item = store[results[i].ref];
          var source = document.getElementById("resultTemplate").innerHTML;
          var template = Handlebars.compile(source);
          var context = {
            title: item.title,
            url: item.url,
            summary: item.content.substring(0, 200),
            authors: item.authors,
            status: item.status,
          };
          var html = template(context);
          searchResults.innerHTML += html
        }
  
        
      } else {
        searchResults.innerHTML = '<p>No results found</p>';
      }
    }
  
    function getQueryVariable(variable) {
      var query = window.location.search.substring(1);
      var vars = query.split('&');
  
      for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split('=');
  
        if (pair[0] === variable) {
          return decodeURIComponent(pair[1].replace(/\+/g, '%20'));
        }
      }
    }
  
    var searchTerm = getQueryVariable('query');
  
    if (searchTerm) {
      document.getElementById('search-box').setAttribute("value", searchTerm);
      document.getElementById('search-btn').classList.add("active");
      document.getElementById('search-form').classList.add("visible");
      document.getElementById('search-box').classList.add("expanded");
  
      // Initalize lunr with the fields it will be searching on. I've given title
      // a boost of 10 to indicate matches on this field are more important.
      var idx = lunr(function () {
        this.field('id');
        this.field('title', { boost: 10 });
        this.field('authors');
        this.field('category');
        this.field('content');
        
        for (var key in window.store) { // Add the data to lunr
            this.add({
              'id': key,
              'title': window.store[key].title,
              'authors': window.store[key].authors,
              'category': window.store[key].category,
              'content': window.store[key].content
            });
        }
      });

      var results = idx.search(searchTerm); // Get lunr to perform a search
      displaySearchResults(results, window.store); // We'll write this in the next section
    }
})();
  